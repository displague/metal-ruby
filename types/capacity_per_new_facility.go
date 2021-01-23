// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// CapacityPerNewFacility capacity per new facility
//
// swagger:model CapacityPerNewFacility
type CapacityPerNewFacility struct {

	// baremetal 1e
	Baremetal1e *CapacityLevelPerBaremetal `json:"baremetal_1e,omitempty"`
}

// Validate validates this capacity per new facility
func (m *CapacityPerNewFacility) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateBaremetal1e(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *CapacityPerNewFacility) validateBaremetal1e(formats strfmt.Registry) error {

	if swag.IsZero(m.Baremetal1e) { // not required
		return nil
	}

	if m.Baremetal1e != nil {
		if err := m.Baremetal1e.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("baremetal_1e")
			}
			return err
		}
	}

	return nil
}

// MarshalBinary interface implementation
func (m *CapacityPerNewFacility) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *CapacityPerNewFacility) UnmarshalBinary(b []byte) error {
	var res CapacityPerNewFacility
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
