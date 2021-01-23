// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"strconv"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// PlanList plan list
//
// swagger:model PlanList
type PlanList struct {

	// plans
	Plans []*Plan `json:"plans"`
}

// Validate validates this plan list
func (m *PlanList) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validatePlans(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *PlanList) validatePlans(formats strfmt.Registry) error {

	if swag.IsZero(m.Plans) { // not required
		return nil
	}

	for i := 0; i < len(m.Plans); i++ {
		if swag.IsZero(m.Plans[i]) { // not required
			continue
		}

		if m.Plans[i] != nil {
			if err := m.Plans[i].Validate(formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("plans" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

// MarshalBinary interface implementation
func (m *PlanList) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *PlanList) UnmarshalBinary(b []byte) error {
	var res PlanList
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
