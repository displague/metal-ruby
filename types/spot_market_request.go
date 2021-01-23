// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// SpotMarketRequest spot market request
//
// swagger:model SpotMarketRequest
type SpotMarketRequest struct {

	// created at
	// Format: date-time
	CreatedAt strfmt.DateTime `json:"created_at,omitempty"`

	// devices max
	DevicesMax int64 `json:"devices_max,omitempty"`

	// devices min
	DevicesMin int64 `json:"devices_min,omitempty"`

	// end at
	// Format: date-time
	EndAt strfmt.DateTime `json:"end_at,omitempty"`

	// facilities
	Facilities *Href `json:"facilities,omitempty"`

	// href
	Href string `json:"href,omitempty"`

	// id
	// Format: uuid
	ID strfmt.UUID `json:"id,omitempty"`

	// instances
	Instances *Href `json:"instances,omitempty"`

	// max bid price
	MaxBidPrice float32 `json:"max_bid_price,omitempty"`

	// project
	Project *Href `json:"project,omitempty"`
}

// Validate validates this spot market request
func (m *SpotMarketRequest) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateCreatedAt(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateEndAt(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateFacilities(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateID(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateInstances(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateProject(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *SpotMarketRequest) validateCreatedAt(formats strfmt.Registry) error {

	if swag.IsZero(m.CreatedAt) { // not required
		return nil
	}

	if err := validate.FormatOf("created_at", "body", "date-time", m.CreatedAt.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *SpotMarketRequest) validateEndAt(formats strfmt.Registry) error {

	if swag.IsZero(m.EndAt) { // not required
		return nil
	}

	if err := validate.FormatOf("end_at", "body", "date-time", m.EndAt.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *SpotMarketRequest) validateFacilities(formats strfmt.Registry) error {

	if swag.IsZero(m.Facilities) { // not required
		return nil
	}

	if m.Facilities != nil {
		if err := m.Facilities.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("facilities")
			}
			return err
		}
	}

	return nil
}

func (m *SpotMarketRequest) validateID(formats strfmt.Registry) error {

	if swag.IsZero(m.ID) { // not required
		return nil
	}

	if err := validate.FormatOf("id", "body", "uuid", m.ID.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *SpotMarketRequest) validateInstances(formats strfmt.Registry) error {

	if swag.IsZero(m.Instances) { // not required
		return nil
	}

	if m.Instances != nil {
		if err := m.Instances.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("instances")
			}
			return err
		}
	}

	return nil
}

func (m *SpotMarketRequest) validateProject(formats strfmt.Registry) error {

	if swag.IsZero(m.Project) { // not required
		return nil
	}

	if m.Project != nil {
		if err := m.Project.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("project")
			}
			return err
		}
	}

	return nil
}

// MarshalBinary interface implementation
func (m *SpotMarketRequest) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *SpotMarketRequest) UnmarshalBinary(b []byte) error {
	var res SpotMarketRequest
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
